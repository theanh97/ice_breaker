from langchain import PromptTemplate
from langchain.llms import OpenAI

from langchain.agents import initialize_agent, Tool, Agent

from Langchain.ice_breaker.tools.tools import get_profile_url


def lookup(name: str) -> str:
    llm = OpenAI(temperature=0, model_name="gpt-3.5-turbo")
    template = """given the full name {name_of_person} I want you to get it me a link to their Linkedin profile page.
                          Your answer should contain only a URL"""

    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedin profile page",
            func=get_profile_url,
            description="useful for when you need get the Linkedin Page URL",
        )
    ]

    agent = initialize_agent(
        tools=tools_for_agent,
        llm=llm,
        agent='zero-shot-react-description',
        verbose=True,
    )
    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )

    linked_profile_url = agent.run(prompt_template.format_prompt(name_of_person=name))
    return linked_profile_url
