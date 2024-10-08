def decode_message( s: str, p: str) -> bool:

# write your code here
    m, n = len(s), len(p)
    
    # dp[i][j] will be True if pattern p[:i] matches message s[:j]
    dp = [[False] * (m + 1) for _ in range(n + 1)]

    # Empty pattern matches empty message
    dp[0][0] = True

    # Handle cases where the pattern starts with '*' and can match empty strings
    for i in range(1, n + 1):
        if p[i - 1] == '*':
            dp[i][0] = dp[i - 1][0]

    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if p[i - 1] == '*':
                # '*' can match zero or more characters
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
            elif p[i - 1] == '?' or p[i - 1] == s[j - 1]:
                # '?' matches one character, or exact match
                dp[i][j] = dp[i - 1][j - 1]

    # Return whether the entire pattern matches the entire message
    return dp[n][m]
