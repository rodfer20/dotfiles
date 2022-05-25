#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

#define MAX_CORES 12

static pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;

void *sync_run(void *arg) {
    // acquire lock
    // pthread_mutex_lock(&mutex);

    // release lock
    // pthread_mutex_unlock(&mutex);
    return NULL;
}

int main(void) {
    int i = 0;

    // create a thread group the size of MAX_CORES
    pthread_t *thread_group = malloc(sizeof(pthread_t) * MAX_CORES);

    // start all threads to begin work
    for (i = 0; i < MAX_CORES; ++i) {
        pthread_create(&thread_group[i], NULL, sync_run, NULL);
    }

    // wait for all threads to finish
    for (i = 0; i < MAX_CORES; ++i) {
        pthread_join(thread_group[i], NULL);
    }

    return EXIT_SUCCESS;
}

