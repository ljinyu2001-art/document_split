def fixed_split(text,chunk_size):

    chunks=[]


    for i in range(0,len(text),chunk_size):

        chunk=text[
            i:i+chunk_size
        ]

        chunks.append(chunk)


    return chunks

def overlap_split(
        text,
        chunk_size,
        overlap
):


    chunks=[]


    start=0


    while start < len(text):


        end=start+chunk_size


        chunk=text[start:end]


        chunks.append(chunk)



        start=end-overlap



        if end>=len(text):
            break



    return chunks




if __name__=="__main__":


    text="ABCDEFGHIJKLMNOPQRSTUVWXYZ"


    result=overlap_split(
        text,
        10,
        3
    )


    for x in result:
        print(x)

import re


def smart_split(text):


    pattern=r"""
    (
    ^第[一二三四五六七八九十\d]+章.*
    |
    ^[一二三四五六七八九十]+、.*
    )
    """


    sections=[]


    parts=re.split(
        pattern,
        text,
        flags=re.MULTILINE | re.X
    )


    title=""


    for part in parts:


        if not part.strip():
            continue


        if re.match(
            pattern,
            part,
            re.MULTILINE | re.X
        ):

            title=part.strip()


        else:

            sections.append(
                {
                    "title":title,
                    "content":part.strip()
                }
            )


    return sections





if __name__=="__main__":


    text="""

第一章 人工智能

人工智能介绍


第二章 机器学习

机器学习介绍


第三章 深度学习

深度神经网络

"""


    result=smart_split(text)


    for r in result:

        print(
            "标题:",
            r["title"]
        )

        print(
            "内容:",
            r["content"]
        )



if __name__=="__main__":


    text="ABCDEFGHIJKLMNOPQRSTUVWXYZ"


    result=fixed_split(
        text,
        5
    )


    for r in result:
        print(r)
