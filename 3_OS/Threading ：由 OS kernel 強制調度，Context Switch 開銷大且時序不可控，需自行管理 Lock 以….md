Threading ：由 OS kernel 強制調度，Context Switch 開銷大且時序不可控，需自行管理 Lock 以避免 Race Condition。
Asyncio： 由 Event Loop 邏輯調度，透過 await 調度控制權，單執行緒低開銷，專門解決高併發 I/O Bound 問題，asyncio 是 function 要自己讓出控制權（await）才會讓 event loop 裡面的其他工作繼續動，所以適合用於 IO-bound 的程式。



asyncio本質上是一個single-thread、cooperative multitasking的event loop模型 他解決的問題是…當process丟出I/O request時 不要傻等I/O做完才繼續跑 而是先去跑別的task 所以它的concurrency來源是I/O wait time的重疊 不是CPU的並行 而asyncio的scheduling是由code主動讓出不是像multithreading那樣由kernel調度 所以asyncio其實更是適合I/O bound的task


