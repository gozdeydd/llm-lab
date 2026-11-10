cat > notes.md << 'EOF'
# Bug Journal

## Gün 1
- **Vim'de kaldım:** `git commit` `-m` olmadan çalışınca Vim açıldı. Çözüm: Esc, `:q!`, Enter. Kalıcı çözüm: `git commit -m "mesaj"`.
- **Push hatası:** "Password authentication is not supported". Çözüm: IDE'nin Git girişi (alternatif: `gh auth login`).

## Gün 2
- **Ollama sürüm uyarısı:** server 0.40.2, client 0.9.2. Muhtemelen iki ayrı kurulum. Kontrol: `which -a ollama`.

## Gün 3
- Sorunsuz.

## Gün 4
- Model hafızasız: geçmişi her istekte biz gönderiyoruz.
- `try/except` girintisi: `while` bloğunun tamamı `try` içine girmeli.
- Küçük model Türkçede zayıf, sistem mesajını İngilizceye çevirdim. Tekrarı `repeat_penalty` ve `num_predict` ile sınırladım.
- `uv init` paket düzeni kurdu, dosyalarım `src/llm_lab/` içinde kalmıştı. `ls -a` ve `find` ile buldum, köke taşıdım.
- `.venv` içindeki `*` yazan `.gitignore` bana ait değildi. Kontrol: `git check-ignore -v dosya`.
EOF