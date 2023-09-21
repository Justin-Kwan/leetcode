// optimal condition variable approach
class Foo {
private:
    std::mutex print_mutex;
    std::condition_variable printed_cv;
    volatile int print_turn;

public:
    Foo(): print_turn{1} {
    }

    void first(function<void()> printFirst) {
        // acquire exclusive access to condition variable to sleep on
        std::unique_lock print_lock(print_mutex);
        printed_cv.wait(print_lock, [&] { return print_turn == 1; });

        // printFirst() outputs "first". Do not change or remove this line.
        printFirst();
        ++print_turn;

        // notify all threads in order to guarantee that second one wakes up
        print_lock.unlock();
        printed_cv.notify_all();
    }

    void second(function<void()> printSecond) {
        std::unique_lock print_lock(print_mutex);
        printed_cv.wait(print_lock, [&] { return print_turn == 2; });

        // printSecond() outputs "second". Do not change or remove this line.
        printSecond();
        ++print_turn;

        // only need to notify remaining sleeping third thread left to print
        print_lock.unlock();
        printed_cv.notify_one();
    }

    void third(function<void()> printThird) {
        std::unique_lock print_lock(print_mutex);
        printed_cv.wait(print_lock, [&] { return print_turn == 3; });

        // printThird() outputs "third". Do not change or remove this line.
        printThird();
        ++print_turn;

        // last thread executes print and does not need to notify any other sleeping threads
        print_lock.unlock();
    }
};
