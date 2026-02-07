
LSM Tree 是一種為了把隨機寫轉成順序寫的儲存結構，  
寫入先進 MemTable，再透過 WAL 保證 durability，  
最後 flush 成 immutable SSTable，  
透過 compaction 控制讀與空間成本。」


OS: page cache / fsync
        ↓
WAL: durability
        ↓
LSM Tree: write optimization
        ↓
Compaction: trade-off control
