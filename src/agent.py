import os
import time
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain.prompts import PromptTemplate

from tools.file_readers import list_files_in_directory, read_names_base_json2
from src.prompt import template

from dotenv import load_dotenv
load_dotenv()

class FileSearchAgent:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash-lite",
            # model="gemini-2.5-flash-lite",
            # model="gemini-1.5-flash", 
            google_api_key=os.getenv("GEMINI_API_KEY")
            )
        
        self.tools = [
            list_files_in_directory,
            read_names_base_json2
        ]

        self.prompt = self._create_system_prompt()



        self.agent = create_tool_calling_agent(
            llm=self.llm,
            tools=self.tools,
            prompt=self.prompt
        )

        self.executor = AgentExecutor(
            agent=self.agent,
            tools=self.tools,
            verbose=True,
            early_stopping_method="generate",
            handle_parsing_errors=True
            )
    def _create_system_prompt(self) -> str:
        """Create a system prompt for the agent."""
        return PromptTemplate.from_template(template)
    
    def search(self, query: str, directory: str) -> str:
        """Search for files and read their content based on the query."""
        target_dir = directory or 'files'
        try:
            
            llm_start = time.perf_counter()
            result = self.executor.invoke(
                {"input": query, "target_dir": target_dir}
            )
            llm_end = time.perf_counter()
            llm_time_ms = int((llm_end - llm_start) * 1000)
            print(f"LLM invocation took {llm_time_ms} ms")

            return result['output']
        except Exception as e:
            return f"Error during search: {str(e)}"



