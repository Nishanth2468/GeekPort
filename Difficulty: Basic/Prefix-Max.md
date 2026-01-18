
<img width="1492" height="1186" alt="Screenshot 2026-01-18 8 40 12 PM" src="https://github.com/user-attachments/assets/2c117cfe-5104-43b6-9d12-c5299c108c1b" />

The Python approach for this:

    t = int(input())

    for _ in range(t):
    
      n = int(input())
      a = list(map(int, input().split()))

      max_val = a[0]
      max_idx = 0

      for i in range(n):
          if a[i] > max_val:
              max_val = a[i]
              max_idx = i

      a[0], a[max_idx] = a[max_idx], a[0]

      curr_max = 0
      total = 0

      for x in a:
        curr_max = max(curr_max, x)
        total += curr_max

      print(total)

and simpler implementation:

      t = int(input())

      for _ in range(t) :
        n = int(input())
        a = list(map(int, input().split()))

        print(max(a) * n)
