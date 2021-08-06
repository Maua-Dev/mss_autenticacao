import pytest
import jwt


@pytest.fixture
def testeModelJWT():
    return [
        jwt.encode(
            payload={
                "sub": "1234567890",
                "name": "John Doe",
                "iat": 1516239022
                },
            key="your-256-bit-secret"
        )
    ]
    
# Compara com JWT do site jwt.io. 
def testeCompararJWT(testeModelJWT): 
    payloadData = {
        "sub": "1234567890",
        "name": "John Doe",
        "iat": 1516239022
    }
    secret = "your-256-bit-secret"
    token = jwt.encode(
        payload=payloadData,
        key=secret
    )
    
    assert token == testeModelJWT[0]
    
@pytest.mark.xfail
def testeCompararJWTFail(testeModelJWT):
    payloadData = {
    }
    secret = "your-256-bit-secret"
    token = jwt.encode(
        payload=payloadData,
        key=secret
    )
    
    assert token == testeModelJWT[0]

@pytest.mark.xfail
def testeAssertFalse():
    assert False
    