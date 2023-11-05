dic_list = []
def binary_search(element, some_list, start_index=0, end_index=None, count=1):
    if end_index == None:
        end_index = len(some_list) - 1
    if start_index > end_index:
        dic_list.append("짜잔~ 없습니다!")
        return None
    mid = (start_index + end_index) // 2

    if (element < some_list[mid]):
        info_dic = {"source" : count, "target" : count+1, "start_index" : start_index, "end_index" : end_index, "mid" : mid, "type" : "call"}
        dic_list.append(info_dic)
        binary_search(element, some_list, start_index, mid - 1, count+1)
        info_dic = {"source" : count+1, "target" : count, "start_index" : start_index, "end_index" : end_index, "mid" : mid, "type" : "return"}
        dic_list.append(info_dic)
    elif (element > some_list[mid]):
        info_dic = {"source" : count, "target" : count+1, "start_index" : start_index, "end_index" : end_index, "mid" : mid, "type" : "call"}
        dic_list.append(info_dic)
        binary_search(element, some_list, mid + 1, end_index, count+1)
        info_dic = {"source" : count+1, "target" : count, "start_index" : start_index, "end_index" : end_index, "mid" : mid, "type" : "return"}
        dic_list.append(info_dic)
    else:
        info_dic = {"source" : count, "target" : count+1, "start_index" : start_index, "end_index" : end_index, "mid" : mid, "type" : "call"}
        dic_list.append(info_dic)
        info_dic = {"source" : count+1, "target" : count, "start_index" : start_index, "end_index" : end_index, "mid" : mid, "type" : "return"}
        dic_list.append(info_dic)

binary_search(0, [0,1,2,3,4,5])

for i in dic_list:
    print(i)