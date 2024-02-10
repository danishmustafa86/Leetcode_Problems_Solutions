class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for i in emails:
            local, domain=i.split("@")
            local=local.split("+")[0]
            local=local.replace(".","")
            unique.add((local,domain))
        return len(unique)