import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils import ArgumentParser, ConfigLoader, LOG
from model import GLMModel, OpenAIModel
from translator import PDFTranslator

if __name__ == "__main__":
    # argument_parser = ArgumentParser()
    # args = argument_parser.parse_arguments()
    # config_loader = ConfigLoader(args.config)

    # config = config_loader.load_config()

    # model_name = args.openai_model if args.openai_model else config['OpenAIModel']['model']
    # api_key = args.openai_api_key if args.openai_api_key else config['OpenAIModel']['api_key']
    config_loader = ConfigLoader("openai-translator/config.yaml")
    config = config_loader.load_config()

    if config['OpenAIModel']['if_use']:
        api_key = config['OpenAIModel']['api_key']
        model_name = config['OpenAIModel']['model']
        model = OpenAIModel(model=model_name, key=api_key)
    else:
        api_key = config['GLMModel']['api_key']
        model_name = config['GLMModel']['model']
        model = GLMModel(model=model_name, key=api_key)

    pdf_file_path = config['common']['book']
    file_format = config['common']['file_format']

    # 实例化 PDFTranslator 类，并调用 translate_pdf() 方法
    translator = PDFTranslator(model)
    translator.translate_pdf(pdf_file_path, file_format)
