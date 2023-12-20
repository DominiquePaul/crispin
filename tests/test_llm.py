from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from crispin.llm import get_all_gpts

def test_get_all_gpts():
    assert get_all_gpts() == None
