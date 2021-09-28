class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = {''}
        
        for email in emails:
            
            local, domain =  email.split('@')
            local_actual = "".join(local.split('.')).split('+')[0]
            unique.add(local_actual + '@' + domain)
        
        return len(unique) - 1
        