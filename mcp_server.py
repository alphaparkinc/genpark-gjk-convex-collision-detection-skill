import sys
import json
from client import GJK2D

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "gjk_collision_test",
                        "description": "Test collision between two 2D convex polygons using GJK",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "poly1": {
                                    "type": "array",
                                    "items": {"type": "array", "items": {"type": "number"}}
                                },
                                "poly2": {
                                    "type": "array",
                                    "items": {"type": "array", "items": {"type": "number"}}
                                }
                            },
                            "required": ["poly1", "poly2"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "gjk_collision_test":
            p1 = [tuple(p) for p in args["poly1"]]
            p2 = [tuple(p) for p in args["poly2"]]
            collided = GJK2D.check_collision(p1, p2)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps({"collided": collided})}]}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        if line.strip():
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
