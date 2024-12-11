class StrMixin:
    def __str__(self) -> str:
        if hasattr(self, "name"):
            return str(self.name)
        if hasattr(self, "title"):
            return str(self.title)
        return super().__str__()