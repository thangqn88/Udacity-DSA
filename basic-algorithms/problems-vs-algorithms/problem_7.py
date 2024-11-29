"""
Problem 7: Request Routing in a Web Server with a Trie

This module implements an HTTPRouter using a Trie data structure.

The HTTPRouter takes a URL path like "/", "/about", or 
"/blog/2019-01-15/my-awesome-blog-post" and determines the appropriate handler 
to return. The Trie is used to efficiently store and retrieve handlers based on 
the parts of the path separated by slashes ("/").

The RouteTrie stores handlers under path parts, and the Router delegates adding 
and looking up handlers to the RouteTrie. The Router also includes a not found 
handler for paths that are not found in the Trie and handles trailing slashes 
to ensure requests for '/about' and '/about/' are treated the same.

You sould implement the function bodies the function signatures. Use the test 
cases provided below to verify that your algorithm is correct. If necessary, 
add additional test cases to verify that your algorithm works correctly.
"""

from typing import Optional

class RouteTrieNode:
    """
    A node in the RouteTrie, representing a part of a route.

    Attributes:
    children (dict): A dictionary mapping part of the route to the corresponding RouteTrieNode.
    handler (Optional[str]): The handler associated with this node, if any.
    """
    def __init__(self, handler=None):
        """
        Initialize a RouteTrieNode with an empty dictionary for children and no handler.
        """
        self.children = {}
        self.handler = handler

    def insert(self, path_part):
        # Insert the node
        if path_part not in self.children:
            self.children[path_part] = RouteTrieNode()
        
        

class RouteTrie:
    """
    A trie (prefix tree) for storing routes and their handlers.

    Attributes:
    root (RouteTrieNode): The root node of the trie.
    """
    def __init__(self, root_handler: str):
        self.root = RouteTrieNode()
        self.handler = root_handler


    def insert(self, path_parts: list[str], handler: str) -> None:
        node = self.root
        for path in path_parts:
            if path not in node.children:
                node.insert(path)
            node = node.children[path]
        node.handler = handler

    def find(self, path_parts: list[str]) ->  Optional[str]:
        if self.root is None:
            return self.not_found
        node = self.root
        for part in path_parts:
            if part not in node.children:
                return self.not_found
            node = node.children[part]
        return node.handler

class Router:
    """
    A router to manage routes and their handlers using a RouteTrie.

    Attributes:
    route_trie (RouteTrie): The trie used to store routes and handlers.
    not_found_handler (str): The handler to return when a route is not found.
    """
    def __init__(self, root_handler: str, not_found_handler: str):
        self.root = RouteTrie(root_handler)
        self.handler = root_handler
        self.not_found = not_found_handler if not_found_handler != "" or not_found_handler is not None else "HTTP 404 Page Not Found"

    def add_handler(self, path: str, handler: str) -> None:
        node = self.root
        path_list = self.split_path(path)
        node.insert(path_list, handler)


    def lookup(self, path: str) -> str:
        if path == '/':
            return "It's Root!"
        node = self.root.root
        path_list = self.split_path(path)
        for part in path_list:
            if part not in node.children:
                return "HTTP 404 Page Not Found"
            node = node.children[part]
        if not node.handler:
            return "HTTP 404 Page Not Found"
        return node.handler


    def split_path(self, path: str) -> list[str]:
        path_list = path.split('/')
        # discard the empty strings
        if path_list[0] == '':
            path_list = path_list[1:]
        return path_list


if __name__ == '__main__':
    # create the router and add a route
    router = Router("root handler", "not found handler")
    router.add_handler("/home/about", "about handler")

    # Edge case: Empty path
    print(router.lookup(""))
    # Expected output: 'HTTP 404 Page Not Found'

    # Normal case: Path not found
    print(router.lookup("/home/contact"))
    # Expected output: 'HTTP 404 Page Not Found'

    # Normal case: Path with multiple segments
    print(router.lookup("/home/about/me"))
    # Expected output: 'HTTP 404 Page Not Found'

    # Normal case: Path with exact match
    print(router.lookup("/home/about"))
    # Expected output: 'about handler'
