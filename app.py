import llama_index
from llama_index.readers.file import CSVReader
from llama_index.readers.file import DocxReader
from llama_index.readers.file import EpubReader
from llama_index.readers.file import FlatReader
from llama_index.readers.file import HTMLTagReader
from llama_index.readers.file import HWPReader
from llama_index.readers.file import IPYNBReader
from llama_index.readers.file import ImageCaptionReader
from llama_index.readers.file import ImageReader
from llama_index.readers.file import ImageTabularChartReader
from llama_index.readers.file import ImageVisionLLMReader
from llama_index.readers.file import MarkdownReader
from llama_index.readers.file import MboxReader
from llama_index.readers.file import PDFReader
from llama_index.readers.file import PagedCSVReader
from llama_index.readers.file import PandasCSVReader
from llama_index.readers.file import PptxReader
from llama_index.readers.file import PyMuPDFReader
from llama_index.readers.file import RTFReader
from llama_index.readers.file import UnstructuredReader
from llama_index.readers.file import VideoAudioReader
from llama_index.readers.file import XMLReader
from llama_index.readers.chroma import ChromaReader
from llama_index.readers.web import AsyncWebPageReader
from llama_index.readers.web import BeautifulSoupWebReader
from llama_index.readers.web import KnowledgeBaseWebReader
from llama_index.readers.web import MainContentExtractorReader
from llama_index.readers.web import NewsArticleReader
from llama_index.readers.web import ReadabilityWebPageReader
from llama_index.readers.web import RssNewsReader
from llama_index.readers.web import RssReader
from llama_index.readers.web import SimpleWebPageReader
from llama_index.readers.web import SitemapReader
from llama_index.readers.web import TrafilaturaWebReader
from llama_index.readers.web import UnstructuredURLLoader
from llama_index.readers.web import WholeSiteReader


##LlamaParse
import llama_parse
from llama_parse import LlamaParse
from llama_index.core import SimpleDirectoryReader
# parser = LlamaParse(
#     api_key="llx-...",  # can also be set in your env as LLAMA_CLOUD_API_KEY
#     result_type="markdown",  # "markdown" and "text" are available
#     num_workers=4, # if multiple files passed, split in `num_workers` API calls
#     verbose=True,
#     language="en" # Optionaly you can define a language, default=en
# )
# # sync
# documents = parser.load_data("./my_file.pdf")

# # sync batch
# documents = parser.load_data(["./my_file1.pdf", "./my_file2.pdf"])

# # async
# documents = await parser.aload_data("./my_file.pdf")

# # async batch
# documents = await parser.aload_data(["./my_file1.pdf", "./my_file2.pdf"])
import gradio as gr

def set_api_keys(anthropic_api_key: str, openai_api_key: str):
    """
    Function to securely set API keys. This example prints a confirmation message
    but in a real application, you should set environment variables, store them securely,
    or directly authenticate with your services as needed.
    """
    # For demonstration purposes only. Replace with secure handling as needed.
    os.environ["ANTHROPIC_API_KEY"] = anthropic_api_key
    os.environ["OPENAI_API_KEY"] = openai_api_key
    
    # Returns a confirmation without exposing the keys
    return "API keys updated successfully. Please proceed with your operations."

# Dummy backend function for handling user query
def handle_query(user_query: str) -> str:
    # Placeholder for processing user query
    return f"Processed query: {user_query}"

# Dummy backend function for handling repository input
def handle_repository(repository_link: str) -> str:
    # Placeholder for processing repository input
    return f"Processed repository link: {repository_link}"

# New dummy function for handling synthetic data generation
def handle_synthetic_data(schema_class_name: str, sample_size: int) -> str:
    # Placeholder for generating synthetic data based on the schema class name and sample size
    return f"Synthetic data for schema '{schema_class_name}' with {sample_size} samples has been generated."

# New dummy function for handling file uploads
def handle_file_upload(uploaded_file):
    # Placeholder for processing the uploaded file
    if uploaded_file is not None:
        return f"Uploaded file '{uploaded_file.name}' has been processed."
    return "No file was uploaded."

def main():
    with gr.Blocks() as demo:
        gr.Markdown("### Securely Input API Keys")
        with gr.Row():
            anthropic_api_key_input = gr.Textbox(label="Anthropic API Key", placeholder="Enter your Anthropic API Key", type="password")
            openai_api_key_input = gr.Textbox(label="OpenAI API Key", placeholder="Enter your OpenAI API Key", type="password")
        submit_button = gr.Button("Submit")
        confirmation_output = gr.Textbox(label="Confirmation", visible=False)  # Keep invisible for added security

        submit_button.click(
            fn=set_api_keys,
            inputs=[anthropic_api_key_input, openai_api_key_input],
            outputs=confirmation_output
        )

        with gr.Tab("User Query"):
            with gr.Row():
                user_query_input = gr.Textbox(label="Enter your query/prompt")
            query_button = gr.Button("Submit Query")
            query_output = gr.Textbox()

            query_button.click(
                fn=handle_query,
                inputs=[user_query_input],
                outputs=query_output
            )

        with gr.Tab("Repository Input"):
            with gr.Row():
                repository_link_input = gr.Textbox(label="Enter repository link")
            repository_button = gr.Button("Process Repository")
            repository_output = gr.Textbox()

            repository_button.click(
                fn=handle_repository,
                inputs=[repository_link_input],
                outputs=repository_output
            )

        with gr.Tab("Generate Synthetic Data"):
            with gr.Row():
                schema_input = gr.Textbox(label="Schema Class Name")
                sample_size_input = gr.Number(label="Sample Size", value=100)
            synthetic_data_button = gr.Button("Generate Synthetic Data")
            synthetic_data_output = gr.Textbox()

            synthetic_data_button.click(
                fn=handle_synthetic_data,
                inputs=[schema_input, sample_size_input],
                outputs=synthetic_data_output
            )

        with gr.Tab("Process Data"):
            with gr.Row():
                file_upload = gr.File(label="Upload Data File")
            file_upload_button = gr.Button("Process Uploaded File")
            file_upload_output = gr.Textbox()

            file_upload_button.click(
                fn=handle_file_upload,
                inputs=[file_upload],
                outputs=file_upload_output
            )

    demo.launch()

if __name__ == "__main__":
    main()


    
from dspy.modules.anthropic import Claude
anthropicChat = Claude(model="claude-3-opus-20240229", port=ports, max_tokens=150)

def choose_reader(file_path: str) -> Any:
    """Choose the appropriate reader based on the file extension."""

    ext = os.path.splitext(file_path)[1].lower()
    
    readers: Dict[str, Any] = {
        ".json": JSONFileReader(),
        ".csv": CSVFileReader(),
        ".xlsx": ExcelSheetReader(),
        ".xls": ExcelSheetReader(),
        ".html": HTMLFileReader(),
        ".pdf": PDFMinerReader(),
        # Add more extensions and their corresponding readers as needed...
    }

    return readers.get(ext, None)

def load_documents_from_folder(folder_path: str) -> List[Document]:
    """Loads documents from files within a specified folder"""
    
    documents = []
    for root, _, filenames in os.walk(folder_path):
        for filename in filenames:
            full_path = os.path.join(root, filename)
            
            reader = choose_reader(full_path)

            if reader:
                print(f"Loading document from '{filename}' with {type(reader).__name__}")
                
                try:
                    docs = list(reader.load_data(input_files=[full_path]))
                    documents.extend(docs)
                    
                except Exception as e:
                    print(f"Failed to load document from '{filename}'. Error: {e}")
    # Convert to langchain format
    documents = [ doc.to_langchain_format()
    for doc in documents
    ]                       
    return documents


###RAGAS SUBTITUTION USING DSPY DATA GENERATOR
import random
from typing import List, Optional

from pydantic import BaseModel

import dspy


class descriptionSignature(dspy.Signature):
  field_name = dspy.InputField(desc="name of a field")
  example = dspy.InputField(desc="an example value for the field")
  description = dspy.OutputField(desc="a short text only description of what the field contains")

class SyntheticDataGenerator:
    def __init__(self, schema_class: Optional[BaseModel] = None, examples: Optional[List[dspy.Example]] = None):
        self.schema_class = schema_class
        self.examples = examples

    def generate(self, sample_size: int) -> List[dspy.Example]:
        if not self.schema_class and not self.examples:
            raise ValueError("Either a schema_class or examples must be provided.")
        if self.examples and len(self.examples) >= sample_size:
            print("No additional data generation needed.")
            return self.examples[:sample_size]

        additional_samples_needed = sample_size - (len(self.examples) if self.examples else 0)
        generated_examples = self._generate_additional_examples(additional_samples_needed)

        return self.examples + generated_examples if self.examples else generated_examples

    def _define_or_infer_fields(self):
        if self.schema_class:
            data_schema = self.schema_class.model_json_schema()
            properties = data_schema['properties']
        elif self.examples:
            inferred_schema = self.examples[0].__dict__['_store']
            descriptor = dspy.Predict(descriptionSignature)
            properties = {field: {'description': str((descriptor(field_name=field, example=str(inferred_schema[field]))).description)}
                          for field in inferred_schema.keys()}
        else:
            properties = {}
        return properties

    def _generate_additional_examples(self, additional_samples_needed: int) -> List[dspy.Example]:
        properties = self._define_or_infer_fields()
        class_name = f"{self.schema_class.__name__ if self.schema_class else 'Inferred'}Signature"
        fields = self._prepare_fields(properties)

        signature_class = type(class_name, (dspy.Signature,), fields)
        generator = dspy.Predict(signature_class, n=additional_samples_needed)
        response = generator(sindex=str(random.randint(1, additional_samples_needed)))

        return [dspy.Example({field_name: getattr(completion, field_name) for field_name in properties.keys()})
                for completion in response.completions]

    def _prepare_fields(self, properties) -> dict:
        return {
            '__doc__': f"Generates the following outputs: {{{', '.join(properties.keys())}}}.",
            'sindex': dspy.InputField(desc="a random string"),
            **{field_name: dspy.OutputField(desc=properties[field_name].get('description', 'No description'))
               for field_name in properties.keys()},
        }
# Generating synthetic data via existing examples
generator = SyntheticDataGenerator(examples=existing_examples)
dataframe = generator.generate(sample_size=5)

#Ragas : https://colab.research.google.com/gist/virattt/6a91d2a9dcf99604637e400d48d2a918/ragas-first-look.ipynb
#from ragas.testset.generator import TestsetGenerator
#from ragas.testset.evolutions import simple, reasoning, multi_context

# generator with openai models
# generator = TestsetGenerator.with_openai()

# generate testset
#testset = generator.generate_with_langchain_docs(documents, test_size=10, distributions={simple: 0.5, reasoning: 0.25, multi_context: 0.25})

# visualize the dataset as a pandas DataFrame
#dataframe = testset.to_pandas()
#dataframe.head(10)


#### DSPY APPLICATION LOGIC GOES HERE

## LOADING DATA
%load_ext autoreload
%autoreload 2

# %set_env CUDA_VISIBLE_DEVICES=7
# import sys; sys.path.append('/future/u/okhattab/repos/public/stanfordnlp/dspy')

import dspy
from dspy.evaluate import Evaluate
from dspy.datasets.hotpotqa import HotPotQA
from dspy.teleprompt import BootstrapFewShotWithRandomSearch, BootstrapFinetune
from dsp.modules.lm import LM

class Claude(LM):
    """Wrapper around anthropic's API. Supports both the Anthropic and Azure APIs."""
    def __init__(
            self,
            model: str = "claude-3-opus-20240229",
            api_key: Optional[str] = None,
            api_base: Optional[str] = None,
            **kwargs,
    ):
        super().__init__(model)

        try:
            from anthropic import Anthropic, RateLimitError
        except ImportError as err:
            raise ImportError("Claude requires `pip install anthropic`.") from err
        
        self.provider = "anthropic"
        self.api_key = api_key = os.environ.get("ANTHROPIC_API_KEY") if api_key is None else api_key
        self.api_base = BASE_URL if api_base is None else api_base

        self.kwargs = {
            "temperature": 0.0 if "temperature" not in kwargs else kwargs["temperature"],
            "max_tokens": min(kwargs.get("max_tokens", 4096), 4096),
            "top_p": 1.0 if "top_p" not in kwargs else kwargs["top_p"],
            "top_k": 1 if "top_k" not in kwargs else kwargs["top_k"],
            "n": kwargs.pop("n", kwargs.pop("num_generations", 1)),
            **kwargs,
        }
        self.kwargs["model"] = model
        self.history: list[dict[str, Any]] = []
        self.client = Anthropic(api_key=api_key)

ports = [7140, 7141, 7142, 7143, 7144, 7145]
#llamaChat = dspy.HFClientTGI(model="meta-llama/Llama-2-13b-chat-hf", port=ports, max_tokens=150) (DELETED)
colbertv2 = dspy.ColBERTv2(url='http://20.102.90.50:2017/wiki17_abstracts')

# Instantiate Claude with desired parameters
claude_model = Claude(model="claude-3-opus-20240229")

# Configure dspy settings with Claude as the language model
dspy.settings.configure(rm=colbertv2, lm=claude_model)
#dspy.settings.configure(rm=colbertv2, lm=llamaChat) #Llama change into model based on line 166

dataset = dataframe
trainset = [x.with_inputs('question') for x in dataset.train]
devset = [x.with_inputs('question') for x in dataset.dev]
testset = [x.with_inputs('question') for x in dataset.test]

#len(trainset), len(devset), len(testset)
#trainset[0]

from dsp.utils.utils import deduplicate

#class BasicMH(dspy.Module):
#    def __init__(self, passages_per_hop=3):
#       super().__init__()

#        self.retrieve = dspy.Retrieve(k=passages_per_hop)
#        self.generate_query = [dspy.ChainOfThought("context, question -> search_query") for _ in range(2)]
#        self.generate_answer = dspy.ChainOfThought("context, question -> answer")
    
#    def forward(self, question):
#        context = []
        
#        for hop in range(2):
#            search_query = self.generate_query[hop](context=context, question=question).search_query
#            passages = self.retrieve(search_query).passages
#            context = deduplicate(context + passages)

#        return self.generate_answer(context=context, question=question).copy(context=context)

class BasicMH(dspy.Module):
    def __init__(self, claude_model, passages_per_hop=3):
        super().__init__()

        self.claude_model = claude_model
        self.passages_per_hop = passages_per_hop
    
    def forward(self, question):
        context = []
        
        for hop in range(2):
            # Retrieval using Claude model
            search_results = self.claude_model.search(question, context=context, k=self.passages_per_hop)
            passages = [result.passage for result in search_results]
            context = deduplicate(context + passages)

        # Generation using Claude model
        answer = self.claude_model.generate(context=context, question=question)

        return answer

        
## Compiling using meta-llama/Llama-2-13b-chat-hf
#RECOMPILE_INTO_MODEL_FROM_SCRATCH = False
#NUM_THREADS = 24

#metric_EM = dspy.evaluate.answer_exact_match

#if RECOMPILE_INTO_MODEL_FROM_SCRATCH:
#    tp = BootstrapFewShotWithRandomSearch(metric=metric_EM, max_bootstrapped_demos=2, num_threads=NUM_THREADS)
#    basicmh_bs = tp.compile(BasicMH(), trainset=trainset[:50], valset=trainset[50:200])

#    ensemble = [prog for *_, prog in basicmh_bs.candidate_programs[:4]]

#    for idx, prog in enumerate(ensemble):
#        # prog.save(f'multihop_llama213b_{idx}.json')
#        pass
#if not RECOMPILE_INTO_MODEL_FROM_SCRATCH:
#    ensemble = []

#    for idx in range(4):
#        prog = BasicMH()
#        prog.load(f'multihop_llama213b_{idx}.json')
#        ensemble.append(prog)
#llama_program = ensemble[0]
#RECOMPILE_INTO_MODEL_FROM_SCRATCH = False
#NUM_THREADS = 24

metric_EM = dspy.evaluate.answer_exact_match

if RECOMPILE_INTO_MODEL_FROM_SCRATCH:
    tp = BootstrapFewShotWithRandomSearch(metric=metric_EM, max_bootstrapped_demos=2, num_threads=NUM_THREADS)
    # Compile the Claude model using BootstrapFewShotWithRandomSearch
    claude_bs = tp.compile(Claude(), trainset=trainset[:50], valset=trainset[50:200])

    # Get the compiled programs
    ensemble = [prog for *_, prog in claude_bs.candidate_programs[:4]]

    for idx, prog in enumerate(ensemble):
        # Save the compiled Claude models if needed
        # prog.save(f'multihop_llama213b_{idx}.json')
        pass
else:
    ensemble = []

    for idx in range(4):
        # Load the previously trained Claude models
        claude_model = Claude(model=f'multihop_claude3opus_{idx}.json') #need to prepare this .json file
        ensemble.append(claude_model)

<<<<<<< Updated upstream
# Select the first Claude model from the ensemble
claude_program = ensemble[0]
=======
    def generate_prompt_with_history( text, history, max_length=2048):
        """
        Generate a prompt with history for the deepseek application.
        Args:
            text (str): The text prompt.
            history (list): List of previous conversation messages.
            max_length (int): The maximum length of the prompt.
        Returns:
            tuple: A tuple containing the generated prompt, conversation, and conversation copy. If the prompt could not be generated within the max_length limit, returns None.
        """
        user_role_ind = 0
        bot_role_ind = 1

        # Initialize conversation
        conversation = # ADD DSPY HERE vl_chat_processor.new_chat_template()

        if history:
            conversation.messages = history

        # if image is not None:
        #     if "<image_placeholder>" not in text:
        #         text = (
        #             "<image_placeholder>" + "\n" + text
        #         )  # append the <image_placeholder> in a new line after the text prompt
        #     text = (text, image)

        conversation.append_message(conversation.roles[user_role_ind], text)
        conversation.append_message(conversation.roles[bot_role_ind], "")

        # Create a copy of the conversation to avoid history truncation in the UI
        conversation_copy = conversation.copy()
        logger.info("=" * 80)
        logger.info(get_prompt(conversation))

        rounds = len(conversation.messages) // 2

        for _ in range(rounds):
            current_prompt = get_prompt(conversation)
            # current_prompt = (
            #     current_prompt.replace("</s>", "")
            #     if sft_format == "deepseek"
            #     else current_prompt
            # )

            # if current_prompt.count("<image_placeholder>") > 2:
            #     for _ in range(len(conversation_copy.messages) - 2):
            #         conversation_copy.messages.pop(0)
            #     return conversation_copy
            
            # if torch.tensor(tokenizer.encode(current_prompt)).size(-1) <= max_length:
            #     return conversation_copy

            if len(conversation.messages) % 2 != 0:
                gr.Error("The messages between user and assistant are not paired.")
                return

            try:
                for _ in range(2):  # pop out two messages in a row
                    conversation.messages.pop(0)
            except IndexError:
                gr.Error("Input text processing failed, unable to respond in this round.")
                return None

        gr.Error("Prompt could not be generated within max_length limit.")
        return None

    def to_gradio_chatbot(conv):
        """Convert the conversation to gradio chatbot format."""
        ret = []
        for i, (role, msg) in enumerate(conv.messages[conv.offset :]):
            if i % 2 == 0:
    #             if type(msg) is tuple:
    # #               msg, image = msg
    #                 msg = msg
    #                 if isinstance(image, str):
    #                     with open(image, "rb") as f:
    #                         data = f.read()
    #                     img_b64_str = base64.b64encode(data).decode()
    #                     image_str = f'<video src="data:video/mp4;base64,{img_b64_str}" controls width="426" height="240"></video>'
    #                     msg = msg.replace("\n".join(["<image_placeholder>"] * 4), image_str)
    #                 else:
                #         max_hw, min_hw = max(image.size), min(image.size)
                #         aspect_ratio = max_hw / min_hw
                #         max_len, min_len = 800, 400
                #         shortest_edge = int(min(max_len / aspect_ratio, min_len, min_hw))
                #         longest_edge = int(shortest_edge * aspect_ratio)
                #         W, H = image.size
                #         if H > W:
                #             H, W = longest_edge, shortest_edge
                #         else:
                #             H, W = shortest_edge, longest_edge
                #         image = image.resize((W, H))
                #         buffered = BytesIO()
                #         image.save(buffered, format="JPEG")
                #         img_b64_str = base64.b64encode(buffered.getvalue()).decode()
                #         img_str = f'<img src="data:image/png;base64,{img_b64_str}" alt="user upload image" />'
                #         msg = msg.replace("<image_placeholder>", img_str)
                # ret.append([msg, None])
            else:
                ret[-1][-1] = msg
        return ret
    def to_gradio_history(conv):
        """Convert the conversation to gradio history state."""
        return conv.messages[conv.offset :]


    def get_prompt(conv) -> str:
        """Get the prompt for generation."""
        system_prompt = conv.system_template.format(system_message=conv.system_message)
        if conv.sep_style == SeparatorStyle.DeepSeek:
            seps = [conv.sep, conv.sep2]
            if system_prompt == "" or system_prompt is None:
                ret = ""
            else:
                ret = system_prompt + seps[0]
            for i, (role, message) in enumerate(conv.messages):
                if message:
                    if type(message) is tuple:  # multimodal message
                        message, _ = message
                    ret += role + ": " + message + seps[i % 2]
                else:
                    ret += role + ":"
            return ret
        else:
            return conv.get_prompt

    def predict(text, chatbot, history, top_p, temperature, repetition_penalty, max_length_tokens, max_context_length_tokens, model_select_dropdown,):
        """
        Function to predict the response based on the user's input and selected model.
        Parameters:
        user_text (str): The input text from the user.
        user_image (str): The input image from the user.
        chatbot (str): The chatbot's name.
        history (str): The history of the chat.
        top_p (float): The top-p parameter for the model.
        temperature (float): The temperature parameter for the model.
        max_length_tokens (int): The maximum length of tokens for the model.
        max_context_length_tokens (int): The maximum length of context tokens for the model.
        model_select_dropdown (str): The selected model from the dropdown.
        Returns:
        generator: A generator that yields the chatbot outputs, history, and status.
        """
        print("running the prediction function")
        # try:
        #     tokenizer, vl_gpt, vl_chat_processor = models[model_select_dropdown]

        #     if text == "":
        #         yield chatbot, history, "Empty context."
        #         return
        # except KeyError:
        #     yield [[text, "No Model Found"]], [], "No Model Found"
        #     return

        conversation = generate_prompt_with_history(
            text,
            image,
            history,
            max_length=max_context_length_tokens,
        )
        prompts = convert_conversation_to_prompts(conversation)
        gradio_chatbot_output = to_gradio_chatbot(conversation)

        # full_response = ""
        # with torch.no_grad():
        #     for x in deepseek_generate(
        #         prompts=prompts,
        #         vl_gpt=vl_gpt,
        #         vl_chat_processor=vl_chat_processor,
        #         tokenizer=tokenizer,
        #         stop_words=stop_words,
        #         max_length=max_length_tokens,
        #         temperature=temperature,
        #         repetition_penalty=repetition_penalty,
        #         top_p=top_p,
        #     ):
        #         full_response += x
        #         response = strip_stop_words(full_response, stop_words)
        #         conversation.update_last_message(response)
        #         gradio_chatbot_output[-1][1] = response
        #         yield gradio_chatbot_output, to_gradio_history(
        #             conversation
        #         ),
        "Generating..."

        print("flushed result to gradio")
        # torch.cuda.empty_cache()

        # if is_variable_assigned("x"):
        #     print(f"{model_select_dropdown}:\n{text}\n{'-' * 80}\n{x}\n{'=' * 80}")
        #     print(
        #         f"temperature: {temperature}, top_p: {top_p}, repetition_penalty: {repetition_penalty}, max_length_tokens: {max_length_tokens}"
        #     )

        yield gradio_chatbot_output, to_gradio_history(conversation), "Generate: Success"


    def retry(
        text,
        image,
        chatbot,
        history,
        top_p,
        temperature,
        repetition_penalty,
        max_length_tokens,
        max_context_length_tokens,
        model_select_dropdown,
    ):
        if len(history) == 0:
            yield (chatbot, history, "Empty context")
            return

        chatbot.pop()
        history.pop()
        text = history.pop()[-1]
        if type(text) is tuple:
            text, image = text

        yield from predict(
            text,
            chatbot,
            history,
            top_p,
            temperature,
            repetition_penalty,
            max_length_tokens,
            max_context_length_tokens,
            model_select_dropdown,
        )

class Application:
    def __init__(self):
        self.api_key_manager = APIKeyManager()
        self.data_processor = DataProcessor(source_file="", collection_name="adapt-a-rag", persist_directory="/your_files_here")
        self.claude_model_manager = ClaudeModelManager()
        self.synthetic_data_handler = SyntheticDataHandler()
        self.chatbot_manager = ChatbotManager()
        
    def set_api_keys(self, anthropic_api_key, openai_api_key):
        return self.api_key_manager.set_api_keys(anthropic_api_key, openai_api_key)
>>>>>>> Stashed changes





# LlamaPack example
from llama_index.core.llama_pack import download_llama_pack

# We will show you how to import the agent from these files!

# from llama_index.core.llama_pack import download_llama_pack

# # download and install dependencies
# download_llama_pack("LLMCompilerAgentPack", "./llm_compiler_agent_pack")
# From here, you can use the pack. You can import the relevant modules from the download folder (in the example below we assume it's a relative import or the directory has been added to your system path).

# # setup pack arguments

# from llama_index.core.agent import AgentRunner
# from llm_compiler_agent_pack.step import LLMCompilerAgentWorker

# agent_worker = LLMCompilerAgentWorker.from_tools(
#     tools, llm=llm, verbose=True, callback_manager=callback_manager
# )
# agent = AgentRunner(agent_worker, callback_manager=callback_manager)

<<<<<<< Updated upstream
# # start using the agent
# response = agent.chat("What is (121 * 3) + 42?")
# You can also use/initialize the pack directly.

# from llm_compiler_agent_pack.base import LLMCompilerAgentPack

# agent_pack = LLMCompilerAgentPack(tools, llm=llm)
# The run() function is a light wrapper around agent.chat().

# response = pack.run("Tell me about the population of Boston")
# You can also directly get modules from the pack.

# # use the agent
# agent = pack.agent
# response = agent.chat("task")


# from llama_parse import LlamaParse
# from llama_index.core import SimpleDirectoryReader

# parser = LlamaParse(
#     api_key="llx-...",  # can also be set in your env as LLAMA_CLOUD_API_KEY
#     result_type="markdown",  # "markdown" and "text" are available
#     verbose=True
# )

# file_extractor = {".pdf": parser}
# documents = SimpleDirectoryReader("./data", file_extractor=file_extractor).load_data()

=======
if __name__ == "__main__":
    app = Application()
    app.main()
>>>>>>> Stashed changes
