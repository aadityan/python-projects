class Task:
    def __init__(self, id, title, desc, status='not started'):
        self.id = id
        self.title = title
        self.desc = desc
        self.status = status

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.desc,
            'status': self.status
        }
    
    @classmethod
    def from_dict(cls, task_dict):
        return cls(
            id = task_dict['id'],
            title = task_dict['title'],
            desc = task_dict['description'],
            status = task_dict['status']
        )
    
    def __str__(self):
        return f"ID: {self.id:02d}\nSTATUS: {self.status}\nTITLE: {self.title}\nDESCRIPTION: {self.desc}"