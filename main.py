from loaders import *

from splitter import (
    fixed_split,
    overlap_split,
    smart_split
)

from splitter import smart_split


text=open(
    "data/test.txt",
    encoding="utf-8"
).read()


result=smart_split(text)


for item in result:

    print("================")

    print(
        "标题:",
        item["title"]
    )

    print(
        item["content"]
    )


text=parse_txt(
    "data/test.txt"
)



print("固定长度切分")
print(
    fixed_split(
        text,
        100
    )
)



print("================")


print("带重叠切分")


print(
    overlap_split(
        text,
        100,
        20
    )
)



print("================")


print("智能章节切分")


print(
    smart_split(text)
)

text=parse_json(
    "data/test.json"
)

print(text)

text=parse_txt("data/test.txt")

print(text)

text=parse_word(
    "data/test.docx"
)

print(text)

text=parse_excel(
    "data/test.xlsx"
)

print(text)

text=parse_pdf(
    "data/test.pdf"
)

print(text)
