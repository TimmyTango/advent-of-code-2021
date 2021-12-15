from typing import Dict, List, Set


TunnelMapping = Dict[str, Set[str]]


def read_input_file() -> TunnelMapping:
    tunnel_map: TunnelMapping = {}

    with open('input/day12.txt') as file:
        for line in file:
            a, b = line.rstrip('\n').split('-')

            if a not in tunnel_map:
                tunnel_map[a] = set()
            if b not in tunnel_map:
                tunnel_map[b] = set()

            tunnel_map[a].add(b)
            tunnel_map[b].add(a)

    return tunnel_map


def path_visited_twice(visited: List[str], path: str) -> bool:
    if path == 'start' or path == 'end': return True
    return visited.count(path) == 2


def small_path_visited_twice(visited: List[str]) -> bool:
    counts: Dict[str, int] = {}
    for path in visited:
        if path not in counts:
            counts[path] = 1
        else:
            counts[path] += 1

    for key, value in counts.items():
        if key.islower() and value == 2:
            return True
        
    return False


def crawl(tunnel: TunnelMapping, visited: List[str], current_node: str, completed_paths: List[List[str]], part1: bool = True):
    visited = visited.copy()
    visited.append(current_node)

    options = tunnel[current_node].copy()
    remove_all_small_paths = part1 or small_path_visited_twice(visited)

    for path in visited:
        if path.islower() and path in options:
            if remove_all_small_paths: 
                options.remove(path)
            elif path_visited_twice(visited, path):
                options.remove(path)

    if current_node == 'end':
        completed_paths.append(visited)

    for path in options:
        crawl(tunnel, visited, path, completed_paths, part1)

    return completed_paths



if __name__ == '__main__':
    tunnel = read_input_file()

    finished_paths = crawl(tunnel, [], 'start', [], part1=True)
    print(f'part1 result: {len(finished_paths)}')

    finished_paths2 = crawl(tunnel, [], 'start', [], part1=False)
    print(f'part2 result: {len(finished_paths2)}')
