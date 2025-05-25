import sqlite3
import leo
from classes import *


def _tuple_to_song(info: tuple[str, str, str, str, str]) -> Song:
    return Song(info[0], info[1], info[2], info[3], info[4], following=None)

def _weight_sorted(nodes: list[tuple[int, float]]) -> list[int]:
    liste_filtree = [couple for couple in nodes if couple[1] != 0]
    liste_triee = sorted(liste_filtree, key=lambda x: x[1])
    return [couple[0] for couple in liste_triee]

def get_from_info(title: str, artist: str) -> Song | None:
    with sqlite3.connect("chansons.db") as db:
        cursor = db.cursor()
        cursor.execute(
            "SELECT * FROM chansons WHERE titre = ? AND artiste = ? LIMIT 1",
            (title, artist),
        )

        result = cursor.fetchone()
        if result != None:
            return _tuple_to_song(result)

        return None


def instanciate() -> Playlist:
    # Get the songs
    conn = sqlite3.connect("chansons.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM chansons ORDER BY isrc ASC")
    result = cursor.fetchall()

    # Create graph
    music_graph: Graph[Node] = Graph()
    for line in result:
        new_song = Song(
            isrc=line[0], title=line[1], artist=line[2], duration=line[3], image=line[4]
        )
        new_node: Node = Node(new_song, False)
        music_graph.add_node(new_node)

    music_graph.matrix = leo.trans_matrix

    # Fill the playlist
    playlist = Playlist()

    first_song_info = get_from_info(*leo.start_song)
    if first_song_info == None:
        raise Exception("Unvalid first song")

    song_node: Node | None = None
    for node in music_graph.node_list:
        if node.song.isrc == first_song_info.isrc:
            song_node = node
            break

    # Check if we found the first song
    if song_node == None:
        raise Exception("Unvalid first song")

    stack = Pile()
    stack.empiler(song_node)

    while not stack.est_vide():
        current_node = stack.depiler()
        if current_node.visited:
            continue

        current_node.visited = True
        playlist.append(current_node.song)

        node_idx = music_graph.get_node_index(current_node)
        edges = music_graph.get_edges(node_idx)
        if edges is None:
            continue

        neighbors = []
        for i, value in edges.items():
            neighbor = music_graph.get_node(i)

            if value > 0 and neighbor and not neighbor.visited:
                neighbors.append((i, value))

        sorted_neighbors = _weight_sorted(neighbors)

        for idx in reversed(sorted_neighbors):
            stack.empiler(music_graph.get_node(idx))

    return playlist
