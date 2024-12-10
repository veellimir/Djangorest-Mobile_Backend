class StrMixin:
    def __str__(self) -> str:
        if hasattr(self, "name"):
            return str(self.name)
        return super().__str__()