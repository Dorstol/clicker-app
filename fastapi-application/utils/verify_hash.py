import hashlib
import hmac


async def verify_hash(request):
    data = request.query_params.dict()

    secret_key = "7307113634:AAEdbmgh6_6rpOc4Qy7VrMGcm4zR2ozdtdE".encode()
    data_check_string = "\n".join(
        f"{k}={v}" for k, v in sorted(data.items()) if k != "hash"
    )
    calculated_hash = hmac.new(
        secret_key, data_check_string.encode(), hashlib.sha256
    ).hexdigest()

    return calculated_hash
