from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import MessagesPlaceholder

def prompt_template():
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system",
             """
            You are a helpful assistant that generates engaging Instagram Reel scripts based on a given topic.
            Write a 90-second Instagram Reel script.

            Topic: {topic}

            Structure:
            1. Welcome and introduction
            2. Hook
            3. Elaborate explanation 
            4. How the {topic} works
            5. CTA
                
            Guidelines:
            - The script should be concise and engaging, suitable for a 90-second Reel.
            - Use a conversational tone to connect with the audience.
            - Include a hook at the beginning to grab attention.
            - Provide clear and informative content about the topic.
            - End with a strong call-to-action (CTA) to encourage viewer interaction.
            - Be a little technical; But also keep it simple and relatable.

            Keep sentences clear.
            Give the sentences in paragraphs. 
            And do not number them or split them according to the structure. Avoid the use of emojis. Avoid using hashtags. Avoid using the same word repeatedly. Use a variety of words to make the script more engaging.
            Medium pacing.
            Dont mention about the script and the reel. 
            Conversational tone."""
             ),
             ("human"
              #"{input}"
              )
        ]
    )
    return prompt