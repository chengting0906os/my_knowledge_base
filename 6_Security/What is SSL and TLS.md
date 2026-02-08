# What is SSL / TLS

|                      | SSL                             | TLS                                                                         |
| -------------------- | ------------------------------- | --------------------------------------------------------------------------- |
| Full Name            | Secure Sockets Layer            | Transport Layer Security                                                    |
| Version              | 1.0, 2.0, 3.0 (all deprecated)  | 1.0, 1.1, 1.2, 1.3 (successor of SSL)                                       |
| Status               | Deprecated                      | 1.2 and 1.3 actively used                                                   |
| Security             | Vulnerable (POODLE, Heartbleed) | Stronger algorithms, fewer vulnerabilities                                  |
| Encryption           | RC4, DES, 3DES, AES             | AES, ChaCha20, Camellia                                                     |
| Hash Functions       | MD5, SHA-1                      | SHA-256, SHA-384, SHA-512                                                   |
| Key Exchange         | RSA, Diffie-Hellman             | RSA, Diffie-Hellman, ECC                                                    |
| Authentication       | MAC (ad-hoc)                    | HMAC                                                                        |
| Alert Messages       | Only 2 types, unencrypted       | Encrypted, more diverse                                                     |
| Handshake            | Complex and slow                | Fewer steps, faster connection                                              |
| Key Features         | Symmetric + Asymmetric + MAC    | Symmetric + Asymmetric + MAC + Perfect Forward Secrecy + Session Resumption |
| TLS 1.3 Improvements |                                 | Zero-RTT, pre-shared keys, removed all legacy ciphers                       |

---

## Quiz

1. What does SSL stand for? What does TLS stand for?
2. Why is SSL deprecated? Name two known vulnerabilities.
3. What hash functions does TLS use instead of MD5 and SHA-1?
4. What is the difference between MAC and HMAC?
5. What is Perfect Forward Secrecy and why does it matter?
6. What are the key improvements in TLS 1.3?
7. What is Zero-RTT and what trade-off does it introduce?

---

## Reference

- [Explore the Differences Between TLS and SSL](https://medium.com/@redswitches/explore-the-differences-between-tls-and-ssl-96355b7c73a9)
