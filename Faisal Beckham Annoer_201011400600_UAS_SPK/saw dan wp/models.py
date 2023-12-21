from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass

class Iphone(Base):
    __tablename__ = "iphone"
    brand : Mapped[str] = mapped_column(primary_key=True)
    ram : Mapped[str]
    battery : Mapped[str]
    processor : Mapped[str]
    kamera : Mapped[str]
    harga : Mapped[int]

    def __repr__(self) -> str :
        return f"brand={self.brand}, ram={self.ram}, battery={self.battery}, processor={self.processor}, kamera={self.kamera}, kamera={self.kamera}, harga={self.harga}"

