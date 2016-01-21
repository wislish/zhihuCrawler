# -*- coding: utf-8 -*-


from zhihu import User
import Queue 
initial_page = "https://www.zhihu.com/people/zhi-yu-63"







def store(user_url):
    user = User(user_url)
    

    return user

def main():
    url_queue = Queue.Queue()
    seen = set()
    seen.insert(initial_page)
    url_queue.put(initial_page)

    while(True): 
        if url_queue.size()>0:
            current_url = url_queue.get()    
            store(user_url)

            for next_url in extract_urls(current_url): 
                if next_url not in seen（BLOOMFILTER）:      
                    seen.put(next_url)
                    url_queue.put(next_url)
        else:
            break






if __name__ == '__main__':
    main()