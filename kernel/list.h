#pragma once

struct list {
    struct list *next;
    struct list *prev;
};

void           lst_init(struct list*);
void           lst_remove(struct list*);
void           lst_push(struct list*, void *);
void*          lst_pop(struct list*);
void           lst_print(struct list*);
int            lst_empty(struct list*);