from autogen import UserProxyAgent, config_list_from_json
from autogen.agentchat.contrib.capabilities.teachability import Teachability
from autogen import ConversableAgent  # As an example


config_list=[
        {
            "model": "StarCoder",
            "base_url": "http://localhost:1234/v1",
            "api_type": "open_ai",
            "api_key": "NULL",
        }
    ]

llm_config={
  "seed": 42,
  "config_list": config_list,
  "temperature": 0,
}

# Start by instantiating any agent that inherits from ConversableAgent, which we use directly here for simplicity.
teachable_agent = ConversableAgent(
    name="teachable_agent",  # The name can be anything.
    llm_config=llm_config
)

# Instantiate a Teachability object. Its parameters are all optional.
teachability = Teachability(
    reset_db=False,  # Use True to force-reset the memo DB, and False to use an existing DB.
    path_to_db_dir="./tmp/interactive/teachability_db"  # Can be any path, but teachable agents in a group chat require unique paths.
)

# Now add teachability to the agent.
teachability.add_to_agent(teachable_agent)

# For this test, create a user proxy agent as usual.
user = UserProxyAgent("user", human_input_mode="ALWAYS")

# This function will return once the user types 'exit'.
teachable_agent.initiate_chat(user, message="Hi, I'm a teachable user assistant! What's on your mind?")