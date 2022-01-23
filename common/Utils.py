def GetTypeOfInput(input):
    try:
        # Convert it into integer
        val = int(input)
        return 'int'
    except ValueError:
        try:
            # Convert it into float
            val = float(input)
            return 'float'
        except ValueError:
            return 'str'