from typing import List, Dict, Tuple

from ...pipeline import Lemmatizer
from ...tokens import Token
from ...symbols import NOUN, VERB, ADJ, NUM, DET, PRON, ADP, AUX, ADV, POS, PUNCT, SCONJ, CCONJ


class AncientGreekLemmatizer(Lemmatizer):
    # This lemmatizer implements lookup lemmatization based on the Polish previous code
    # and it uses Morpheus ancient greek corpus to draw the lemma files. 
    
    """
    Anciente Greek language lemmatizer works as follows:    
    1) check the index table, if the word is there is already a lemma. Return it.   
    2) check the lookup table of the given pos. if the word is there, return it.   
    3) return the given word in lowercase. 
    """

    univ_pos_name_variants = {
        NOUN: "noun",
        "NOUN": "noun",
        "noun": "noun",
        VERB: "verb",
        "VERB": "verb",
        "verb": "verb",
        AUX: "verb",
        "AUX": "verb",
        "aux": "verb",
        ADJ: "adj",
        "ADJ": "adj",
        "adj": "adj",
        ADV: "adv",
        "ADV": "adv",
        "adv": "adv",
        PRON: "pron",
        "PRON": "pron",
        "pron": "pron",
        DET: "det",
        "DET": "det",
        "det": "det",
        ADP: "adp",
        "ADP": "adp",
        "adp": "adp",
        NUM: "num",
        "NUM": "num",
        "num": "num",
        "X" : "x", 
        "x" : "x",
        "ADP" : "adp",
        "adp" : "adp",
        "intj" : "intj",
        "INTJ": "intj",
        "sconj" : "sconj",
        "SCONJ" : "sconj", 
        "part" : "part",
        "PART" : "part",
        "punct" : "punct",
        "PUNCT" : "punct",
        "cconj" : "cconj",
        "CCONJ": "cconj",
    }

    @classmethod
    def get_lookups_config(cls, mode: str) -> Tuple[List[str], List[str]]:
        if mode == "pos_lookup":
            # fmt: off
            required = [
                "lemma_index","lemma_lookup_det","lemma_lookup_adj",
                "lemma_lookup_adp", "lemma_lookup_cconj", "lemma_lookup_sconj","lemma_lookup_adv",
                "lemma_lookup_intj", "lemma_lookup_noun", "lemma_lookup_num",
                "lemma_lookup_part", "lemma_lookup_pron", "lemma_lookup_verb"
            ]
            # fmt: on
            return (required, [])
        else:
            return super().get_lookups_config(mode)

    def pos_lookup_lemmatize(self, token: Token) -> List[str]:
        string = token.text
        univ_pos = token.pos_
        morphology = token.morph.to_dict()
        #lookup_pos = univ_pos.lower()
        
        string = string.lower()
        
        try:
            univ_pos = self.univ_pos_name_variants[univ_pos]
            #print("Pos is ", univ_pos)
        except KeyError:
            # Because PROPN is not in self.univ_pos_name_variants, proper names
            # are not lemmatized. They are lowercased, however.
            return [string]
            # if string in self.lemma_index.get(univ_pos)            
        
        lookup_pos = univ_pos.lower() # to have the suffix of the filename    
            
        index_table = self.lookups.get_table("lemma_index", {})
        # print("index table", index_table)
        #print("searching index")
        lemma_index = index_table.get(univ_pos, {})
        # string is already lemma
        if string in lemma_index:
    #        print("string in index")
            return [string]
            
        tablename = "lemma_lookup_"+lookup_pos.strip()    
            
        # string corresponds to a key in the lookup table for that univ_pos
        lookup_table = self.lookups.get_table(tablename, {})
        
        #print("lookup table", lookup_table)
        looked_up_lemma = lookup_table.get(string)
        #print("searching ->"+tablename+"<- for ", string, " found ", looked_up_lemma)  # univ_pos
        if looked_up_lemma: # and looked_up_lemma in lemma_index:
            #print("string was found in lemma_lookup_",lookup_pos,".json")
            return [looked_up_lemma]
         
 #       print("it could not be lemmatized")
        return [string]
        
'''
    def lemmatize_adj(
        self, string: str, morphology: dict, lookup_table: Dict[str, str]
    ) -> List[str]:
        # this method utilizes different procedures for adjectives
        # with 'nie' and 'naj' prefixes
        if string[:3] == "nie":
            search_string = string[3:]
            if search_string[:3] == "naj":
                naj_search_string = search_string[3:]
                if naj_search_string in lookup_table:
                    return [lookup_table[naj_search_string]]
            if search_string in lookup_table:
                return [lookup_table[search_string]]
        if string[:3] == "naj":
            naj_search_string = string[3:]
            if naj_search_string in lookup_table:
                return [lookup_table[naj_search_string]]
        return [lookup_table.get(string, string)]

    def lemmatize_verb(
        self, string: str, morphology: dict, lookup_table: Dict[str, str]
    ) -> List[str]:
        # this method utilizes a different procedure for verbs
        # with 'nie' prefix
        if string[:3] == "nie":
            search_string = string[3:]
            if search_string in lookup_table:
                return [lookup_table[search_string]]
        return [lookup_table.get(string, string)]

    def lemmatize_noun(
        self, string: str, morphology: dict, lookup_table: Dict[str, str]
    ) -> List[str]:
        # this method is case-sensitive, in order to work
        # for incorrectly tagged proper names
        if string != string.lower():
            if string.lower() in lookup_table:
                return [lookup_table[string.lower()]]
            elif string in lookup_table:
                return [lookup_table[string]]
            return [string.lower()]
        return [lookup_table.get(string, string)]
        
        '''
