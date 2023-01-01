class Match:
    
    def new_data(data):
        new_data = []
        for dict in data:
            proxy_dict = {}
            del dict["created_at"]
            for k, v in dict.items():
                if dict[k] != False:
                    proxy_dict[k] = v
            new_data.append(proxy_dict)
        return new_data
    
    
    @staticmethod
    def product_compare(d1_data, d2_data):
        d1_list = Match.new_data(d1_data)
        d2 = d2_data
        matched = []
        for d1 in d1_list:
            result = {}
            d1_keys = set(d1.keys())
            d2_keys = set(d2.keys())
            shared_keys = d1_keys.intersection(d2_keys)
            added = d1_keys - d2_keys
            removed = d2_keys - d1_keys
            modified = {o: (d1[o], d2[o]) for o in shared_keys if d1[o] != d2[o]}
            same = set(o for o in shared_keys if d1[o] == d2[o])
            percentage = (100 / (len(d1))) * len(same)
            if percentage > 49:
                result["customer_name"]=d2_data.get("customer_first_name")
                result["customer_last_name"]=d2_data.get("customer_last_name")
                result["customer_phone_number"]=d2_data.get("customer_phone_number")
                result["employee_first_name"]=d2_data.get("employee_first_name")
                result["employee_last_name"]=d2_data.get("employee_last_name")
                result["employee_phone_number"]=d2_data.get("employee_phone_number")
                result["id"]=d1["id"]
                result["same"]=same
                result["match_rate"]=percentage
                matched.append(result)
        return matched






