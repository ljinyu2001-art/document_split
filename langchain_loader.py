from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    JSONLoader,
    UnstructuredWordDocumentLoader,
    UnstructuredExcelLoader
)



def load_pdf(path):

    return PyPDFLoader(path).load()



def load_word(path):

    return UnstructuredWordDocumentLoader(path).load()



def load_excel(path):

    return UnstructuredExcelLoader(path).load()



def load_txt(path):

    return TextLoader(
        path,
        encoding="utf-8"
    ).load()



def load_json(path):

    return JSONLoader(
        file_path=path,
        jq_schema=".",
        text_content=False
    ).load()



if __name__=="__main__":


    tests=[
        ("Word",load_word,"data/test.docx"),
        ("PDF",load_pdf,"data/test.pdf"),
        ("Excel",load_excel,"data/test.xlsx"),
        ("TXT",load_txt,"data/test.txt"),
        ("JSON",load_json,"data/test.json")
    ]


    for name,func,path in tests:

        print("================")
        print(name)

        docs=func(path)


        for doc in docs:

            print(doc.page_content[:200])

            print(doc.metadata)