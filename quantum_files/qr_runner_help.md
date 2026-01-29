# Create a new genome
python run_qr_system.py --create

# Execute the genome
python run_qr_system.py --execute

# Evolve the genome using phi-harmonic principles
python run_qr_system.py --evolve

# Generate QR sequence from genome
python run_qr_system.py --generate

# Display QR sequence as flipbook
python run_qr_system.py --display

# Analyze QR sequence
python run_qr_system.py --analyze

# Run QR worker to capture and execute QR codes
python run_qr_system.py --worker

You can now run the complete system with a simple command:

# Run the complete system
python run_qr_system.py --full-cycle

# Run the integrated system

 python qr_integrated_system.py


# Run the recursive system

 source qr_dna_env/bin/activate && python qr_recursive_main.py --cycles 5
