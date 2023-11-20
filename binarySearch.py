dic_list = []
def binary_search(element, some_list, start_index=0, end_index=None, count=0):
    if (end_index == None):
        end_index = len(some_list) - 1
    
    if (start_index > end_index):
        finded_index = None
        return None
    
    mid = (start_index + end_index) // 2

    if (element in some_list):
        finded_index = some_list.index(element)
    else:
        finded_index = None

    if (element < some_list[mid]):
        info_dic = {"source" : count, "target" : count+1, "start_index" : start_index, "end_index" : end_index, "mid" : mid, "type" : "call"}
        dic_list.append(info_dic)
        binary_search(element, some_list, start_index, mid - 1, count+1)
        
    elif (element > some_list[mid]):
        info_dic = {"source" : count, "target" : count+1, "start_index" : start_index, "end_index" : end_index, "mid" : mid, "type" : "call"}
        dic_list.append(info_dic)
        binary_search(element, some_list, mid + 1, end_index, count+1)
        
    else:
        info_dic = {"source" : count, "target" : count+1, "start_index" : start_index, "end_index" : end_index, "mid" : mid, "type" : "call"}
        dic_list.append(info_dic)

    for i, link in enumerate(dic_list):
            if link["target"] == count:
                dic_list[i]["return_text"] = "finded index is : {}".format(finded_index)

