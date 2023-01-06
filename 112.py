class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for e in emails:
            loc, dom = e.split("@")                                 # get parts of email
            fwd = loc.split("+")[0].replace(".", "") + "@" + dom    # build forward email
            unique.add(fwd)
        return len(unique)
