from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import TokenTextSplitter

from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import SystemMessage
from langchain_core.prompts import (
    ChatPromptTemplate, 
    HumanMessagePromptTemplate,
    PromptTemplate
)
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import (
    ChatOpenAI,
    OpenAIEmbeddings
)
from langchain_chroma.vectorstores import Chroma


loader_pdf = PyPDFLoader("sample_data/US_Constitution.pdf")
docs_list =  loader_pdf.load()

print(docs_list[0].page_content[:500])