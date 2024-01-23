#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return None
    return (len(sentence), sentence[0] if len(sentence) > 0 else None)
