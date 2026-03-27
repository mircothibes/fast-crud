def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200

def test_create_user(client):
    response = client.post("/users", json={"name": "Ana Silva", "email": "ana@example.com"})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Ana Silva"
    assert data["email"] == "ana@example.com"
    assert "id" in data

def test_create_user_duplicate_email(client):
    client.post("/users", json={"name": "Ana Silva", "email": "ana@example.com"})
    response = client.post("/users", json={"name": "Ana Costa", "email": "ana@example.com"})
    assert response.status_code == 400
    assert "already exists" in response.json()["detail"]

def test_list_users(client):
    client.post("/users", json={"name": "Ana Silva", "email": "ana@example.com"})
    client.post("/users", json={"name": "Bruno Lima", "email": "bruno@example.com"})
    response = client.get("/users")
    assert response.status_code == 200
    assert len(response.json()) == 2

def test_get_user(client):
    created = client.post("/users", json={"name": "Ana Silva", "email": "ana@example.com"})
    user_id = created.json()["id"]
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["id"] == user_id

def test_get_user_not_found(client):
    response = client.get("/users/9999")
    assert response.status_code == 404

def test_update_user(client):
    created = client.post("/users", json={"name": "Ana Silva", "email": "ana@example.com"})
    user_id = created.json()["id"]
    response = client.put(f"/users/{user_id}", json={"name": "Ana Costa", "email": "ana.costa@example.com"})
    assert response.status_code == 200
    assert response.json()["name"] == "Ana Costa"

def test_delete_user(client):
    created = client.post("/users", json={"name": "Ana Silva", "email": "ana@example.com"})
    user_id = created.json()["id"]
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 204
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 404
