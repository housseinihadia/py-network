import dns.resolver
target=str(input("Enter domin name / ip for target >> "))
types=["A","AAAA","MX","NS","SOA","SPV","CNAME"]
for record in types:
    d=dns.resolver.query(target,record,raise_on_no_answer=False)
    if d.rrset is not None:
        print(d.rrset)
