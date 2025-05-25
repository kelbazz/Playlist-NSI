from typing import TypeVar, Generic, Optional


class Song:
    def __init__(
        self,
        isrc: str,
        title: str,
        artist: str,
        duration: str,
        image: str,
        following: Optional["Song"] = None,
    ) -> None:
        self.isrc: str = isrc
        self.title: str = title
        self.artist: str = artist
        self.duration: str = duration
        self.img: str = image
        self.next: Optional[Song] = following


class Node:
    def __init__(self, song: Song, visited: bool = False) -> None:
        self.song: Song = song
        self.visited: bool = visited


Content = TypeVar("Content")  # Generic type


class Graph(Generic[Content]):
    def __init__(self) -> None:
        self.node_list: list[Content] = []  # ListeSommets
        self.matrix: list[list[float]] = []  # mat

    def set_bi_edge(self, idx_1: int, idx_2: int, value: float = 1) -> None:
        self.matrix[idx_1][idx_2] = value
        self.matrix[idx_2][idx_1] = value

    def set_edge(self, idx_1: int, idx_2: int, value: float = 1) -> None:
        self.matrix[idx_1][idx_2] = value

    def add_node(self, node: Content) -> int:
        self.node_list.append(node)

        for i in range(len(self.matrix)):
            self.matrix[i].append(0)

        self.matrix.append([0.0] * len(self.node_list))

        # Returns the node index
        return len(self.node_list) - 1

    def get_node_index(self, node: Content) -> int:
        try:
            return self.node_list.index(node)
        except ValueError:
            return -1

    def is_valid_index(self, idx: int) -> bool:
        return 0 <= idx < len(self.node_list)

    def get_node(self, idx: int) -> Content | None:
        if self.is_valid_index(idx):
            return self.node_list[idx]

        return None

    def get_edges(
        self, idx: int, value_range: Optional[tuple[float, float]] = None
    ) -> dict[int, float] | None:
        result = {}

        if not self.is_valid_index(idx):
            return None

        edges = self.matrix[idx]
        for i, value in enumerate(edges):
            if value_range is None or (value_range[0] <= value <= value_range[1]):
                result[i] = value

        return result


class Playlist:
    def __init__(self) -> None:
        self.head: Song | None = None

    def is_empty(self) -> bool:
        return self.head is None

    def insert(self, previous_song: Song, new_song: Song) -> None:
        """insère une nouvelle chanson juste après previous_song"""

        # cas où previous_song est en tête
        if self.head is None:
            tmp = new_song
            tmp.next = self.head
            self.head = tmp
        # cas général
        else:
            current = self.head
            while current.next is not None and current is not previous_song:
                current = current.next

            tmp = new_song
            tmp.next = current.next
            current.next = tmp

    def append(self, song: Song) -> None:
        if self.head is None:
            self.head = song
        else:
            current = self.head
            while current.next is not None:
                current = current.next

            print(current.artist, song.artist)
            current.next = song

    def __len__(self) -> int:
        if self.head == None:
            return 0
        else:
            t = 1
            current = self.head
            while current.next is not None:
                t += 1
                current = current.next
            return t

    def __repr__(self) -> str:
        result = "╒════════════╕\n"
        result += "│  Playlist  │\n"
        result += "╞════════════╛\n"

        current = self.head
        if current is None:
            result += f"└ \x1b[1;31mEmpty\x1b[0;0m"
        else:
            while current.next is not None:
                result += f"├ * {current.title}\n"
                current = current.next

            result += f"└ * {current.title}"

        return result


class Pile:
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        return len(self.contenu) == 0

    def empiler(self, v):
        self.contenu.append(v)

    def depiler(self):
        if not self.est_vide():
            return self.contenu.pop()

        else:
            raise Exception("saisie incorrecte")
