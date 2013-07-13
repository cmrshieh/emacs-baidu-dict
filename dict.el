(defun dict-search-wordap (&optional word)

"Use python script dict to look up word under point"

(interactive)

(or word (setq word (current-word)))

(shell-command (format "python ~/Dropbox/emacs_setting/site-lisp/bdict.py %s" word)))

(global-set-key (kbd "C-c d") 'dict-search-wordap)

(provide 'dict)