from langchain_community.document_loaders import YoutubeLoader

def youtube_load(video_id):

    """
    Give transcript List[Document]

    """

    transcript = YoutubeLoader(video_id="o126p1QN_RI",language=["en"])
    docs = transcript.load()
    
    return docs

    



