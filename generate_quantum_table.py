"""Generate a complete ASCII art periodic table for all 434 quantum elements."""

def generate_element_row(start_num, elements):
    """Generate a row of elements in ASCII art format."""
    row = []
    header = f"     ||"
    for i in range(10):  # 10 elements per row
        element = elements[start_num + i] if start_num + i < len(elements) else None
        if element:
            header += f"     {start_num + i + 1:2d}              ||"
    row.append(header)
    
    # ASCII art box for each element
    for line in range(5):
        if line == 0:
            art_line = "     ||"
            for i in range(10):
                if start_num + i < len(elements):
                    art_line += " ____   _       2||"
        elif line == 1:
            art_line = "     ||"
            for i in range(10):
                if start_num + i < len(elements):
                    art_line += "||  _ \\ | |__   8||"
        elif line == 2:
            art_line = "     ||"
            for i in range(10):
                if start_num + i < len(elements):
                    art_line += "|| |_) || '_ \\  18||"
        elif line == 3:
            art_line = "     ||"
            for i in range(10):
                if start_num + i < len(elements):
                    art_line += "||  __/ | |_) | 21||"
        else:
            art_line = "     ||"
            for i in range(10):
                if start_num + i < len(elements):
                    art_line += "||_|    \\____/   8||"
        row.append(art_line)
    
    # Element symbols and properties
    symbols = "     |"
    masses = "     |"
    stabilities = "     |"
    for i in range(10):
        if start_num + i < len(elements):
            element = elements[start_num + i]
            symbols += f"{element['symbol']:<16}|"
            masses += f"{element['mass']:<16.3f}|"
            stabilities += f"Stb: {element['stability']:<10.3f}|"
    row.extend([symbols, masses, stabilities])
    
    return row

def generate_complete_table():
    """Generate the complete periodic table with all 434 elements."""
    elements = []
    
    # Generate element data (this would normally come from your quantum system)
    for i in range(434):
        mass = i * 1.618034 + 2.0  # φ-based mass progression
        stability = min(1.0, 0.8 + (i * 0.0005))  # Increasing stability
        element = {
            'symbol': f'Qe{i+1}',
            'mass': mass,
            'stability': stability
        }
        elements.append(element)
    
    # Generate the table row by row
    table = []
    for start_num in range(0, 434, 10):
        row = generate_element_row(start_num, elements)
        table.extend(row)
        table.append("-----+" + "------------------+" * 10)
    
    return table

if __name__ == '__main__':
    table = generate_complete_table()
    with open('Complete_Quantum_Table.txt', 'w') as f:
        f.write('\n'.join(table))
