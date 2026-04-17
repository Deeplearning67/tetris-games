# Classic Tetris — 经典俄罗斯方块

> Three implementations of the classic Tetris game: HTML (desktop), HTML (mobile+desktop), and Python/Pygame.

一个项目，三种实现，涵盖桌面网页、手机触屏、Python桌面版。

---

## 📁 Project Structure / 项目结构

```
tetris-games/
├── README.md
├── LICENSE
├── src/
│   ├── tetris.html         # Computer version / 电脑版
│   ├── tetris-phone.html   # Dual-platform version (PC + Mobile) / 双端版
│   └── tetris.py           # Python Pygame version / Python版
└── screenshots/            # Game screenshots / 游戏截图
```

---

## 🎮 Games / 游戏介绍

### 1. Computer Version — 电脑版
`src/tetris.html`

Classic desktop Tetris game, pure HTML + JavaScript, runs directly in any browser. No dependencies needed.

经典桌面版，纯HTML+JS，双击浏览器打开即可玩。

**Controls / 操作：**
- ← → Move / 移动
- ↑ Rotate / 旋转
- ↓ Accelerate / 加速
- Space Drop instantly / 立即落地

---

### 2. Dual-Platform Version — 双端版
`src/tetris-phone.html`

Works on both desktop and mobile. Desktop uses keyboard controls; mobile detects touch and shows on-screen buttons automatically.

电脑手机都能玩。电脑用方向键，手机自动显示触屏按钮。

**Controls / 操作：**
- Desktop: same as above / 电脑：同上
- Mobile: tap buttons on screen / 手机：点击屏幕按钮

---

### 3. Python Version — Python版
`src/tetris.py`

Built with Pygame. Requires `pygame` library. Install and run:

```bash
pip install pygame
python tetris.py
```

基于 Pygame 的桌面版，需要先安装 pygame 库。

**Controls / 操作：**
- ← → Move / 移动
- ↑ Rotate / 旋转
- ↓ Accelerate / 加速
- Space Drop instantly / 立即落地

---

## 📖 About Tetris / 关于俄罗斯方块

Tetris is a classic puzzle game invented by Alexey Pajitnov in 1984. The goal is to arrange falling tetromino blocks to complete and clear horizontal lines. The game ends when the blocks stack up to the top.

俄罗斯方块由俄罗斯程序员阿列克谢·帕吉特诺夫于1984年发明。玩家通过旋转和移动下落的方块，使其填满一行后消除得分。方块堆叠到顶部时游戏结束。

---
<img width="821" height="1215" alt="捕获" src="https://github.com/user-attachments/assets/715b5bf9-d1f7-4de8-a79d-78d3c37bf094" />


## 📄 License / 许可证

MIT License — feel free to use, modify, and share.
