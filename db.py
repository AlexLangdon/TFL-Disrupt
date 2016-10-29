
class db_obj() :
    temp_nums = ["+447805081856", "+447480132452", "+447515067000", "447739586816", "+447809358784"]

    db_store = [
                    {"bakerloo": {"status_text": "N/A", "nums": []}},
                    {"central": {"status_text": "N/A", "nums": [temp_nums[4]]}},
                    {"circle": {"status_text": "N/A", "nums": []}},

                    {"district": {"status_text": "N/A", "nums": []}},
                    {"hammersmith-city": {"status_text": "N/A", "nums": []}},
                    {"jubilee": {"status_text": "N/A", "nums": []}},

                    {"metropolitan": {"status_text": "N/A", "nums": []}},
                    {"northern": {"status_text": "N/A", "nums": []}},
                    {"piccadilly": {"status_text": "N/A", "nums": []}},

                    {"victoria": {"status_text": "N/A", "nums": []}},
                    {"waterloo-city": {"status_text": "N/A", "nums": []}}
                ]

    def add_num(self,line,num) :
        if not num in self.db_store[line]["nums"] :
            self.db_store[line]["nums"] += num