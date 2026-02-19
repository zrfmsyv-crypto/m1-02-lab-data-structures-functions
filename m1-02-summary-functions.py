def problem(t):
    keys = ['ticket_id','customer_id','category','resolution_minutes','escalated']
    not_it = []
    for k,v in enumerate(t):
        for i in keys:
            if i not in v:
                not_it.append(i)
                break
    return not_it, len(not_it)


def missing(t):
    none_lst = []
    for i in t:
        if i["resolution_minutes"] == None:
            none_lst.append(i)
    return none_lst,len(none_lst)


def cleaned(t):
    clean_n = []
    for i in t:
        ticket_n = i.copy()
        if ticket_n["resolution_minutes"] is None:
            ticket_n["resolution_minutes"] = not_none/200
        ticket_n["category"] = ticket_n["category"].strip().lower()
        clean_n.append(ticket_n)
    return clean_n

def summary(t):
    count = {}
    d = {}
    for i in t:
        name = i["category"]
        avg_time = i["resolution_minutes"]
        if name not in d:
            d[name]=0
            count[name]=0
        d[name] += avg_time
        count[name]+=1
    avg_per_cate = {}
    for name in d:
        avg_per_cate[name] = d[name]/count[name]

    return avg_per_cate

def ticket_count(t):
    count_t = {}
    for i in t:
        customer = i["customer_id"]
        if customer not in count_t:
            count_t[customer] = 0
        count_t[customer]+=1
    return count_t



# Escalation rate overall and by category
def over(t):
    escalat_count = {}
    catg = {}
    for i in t:
        cat = i["category"]
        new = i["escalated"]
        if cat not in escalat_count:
            escalat_count[cat] = 0
            catg[cat] = 0
        escalat_count[cat] += int(new)
        catg[cat] +=1 
    rate= {cat: escalat_count[cat]/catg[cat] 
                         for cat in escalat_count}

    overall = sum(escalat_count.values())/sum(catg.values())
    return rate, overall


def final(t):
    avg_resolution = summary(t)
    count_of_ticket = ticket_count(t)
    rate_overall = over(t)
    report = {
        "Average resolution time per category": avg_resolution,
        "Count of tickets per customer": count_of_ticket,
        "Escalation rate overall and by category": rate_overall
    }
    return report