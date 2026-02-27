# Symmetric vs Asymmetric Encryption

## Overview

- Symmetric Encryption（對稱式加密）：加密與解密使用同一把金鑰。
- Asymmetric Encryption（非對稱式加密）：使用一對金鑰（Public Key / Private Key）。

## How They Work Together (Very Important)

實務上通常是「混合式」：

1. Use asymmetric crypto to securely exchange a session key.
2. Use symmetric crypto for actual data transfer.

Example: HTTPS/TLS handshake uses asymmetric methods to establish keys, then uses symmetric ciphers for the session.

## Interview 30-second Version

對稱式加密同一把 key，速度快，適合大量資料；非對稱式加密用公私鑰，速度慢但解決金鑰交換並可做簽章。實務上兩者會一起用：先用非對稱交換 session key，再用對稱加密傳資料（例如 TLS）。

## Quick Check

1. Why is symmetric encryption faster?
2. Why do we still need asymmetric encryption if it is slower?
3. In HTTPS, which part usually uses asymmetric vs symmetric encryption?
