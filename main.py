from pypdf import PdfReader
import glob


def find_word_in_pdf(path, look_up_text):

    try:
        reader = PdfReader(path)
        for page_number, page in enumerate(reader.pages):
            text = page.extract_text()
            if text and look_up_text.lower() in text.lower():
                return page_number
    except Exception as e:
        print(f"Error processing {path}: {e}")
    return None


def get_pdf_paths(directory_path):
    return glob.glob(f'{directory_path}*.pdf')


def main(directory_path, look_up_text):
    for path in get_pdf_paths(directory_path):
        result = find_word_in_pdf(path, look_up_text)
        if result is not None:
            print(f"Found '{look_up_text}' in {path} on page {result + 1}")


directory_path = '/home/andrew/Downloads/Telegram_Desktop/ChatExport_2023-12-16/files/'
look_up_text = 'Jenkins'


if __name__ == "__main__":
    main(directory_path, look_up_text)